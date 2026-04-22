# The Complete Guide to Retrieval-Augmented Generation (RAG)
### From Beginner to System Designer

---

## Table of Contents

| # | Section | Topics |
|---|---------|--------|
| 1 | **Foundations** | What is RAG, Why it exists, Core concepts |
| 2 | **Core Components** | Embeddings, Vector DBs, Chunking, Pipelines |
| 3 | **RAG Architecture** | End-to-end system design, all flows |
| 4 | **Retrieval Techniques** | BM25, Dense, Hybrid, Re-ranking |
| 5 | **Types of RAG Systems** | Naive → Agentic → Graph → Multi-hop |
| 6 | **Optimization & Scaling** | Latency, Cost, Caching, Sharding |
| 7 | **Evaluation** | Precision, Recall, Faithfulness, Hallucination |
| 8 | **Security & Risks** | Prompt injection, Data leakage |
| 9 | **Practical Design Patterns** | Real systems explained step by step |

---

# SECTION 1: FOUNDATIONS

---

## 1.1 What Is RAG?

**Simple Explanation:**
RAG is a technique that gives an LLM access to external knowledge at the time of answering — without retraining it.

Think of it this way:
- An LLM is like a **smart person who studied a lot** but graduated in 2023.
- They can't know what happened after they left school.
- RAG gives them a **reference book** to look things up before answering.

**The Core Idea:**

```
User asks a question
  → System finds relevant documents
    → Documents are given to the LLM as context
      → LLM answers using both its knowledge AND the retrieved documents
```

**Why the name "Retrieval-Augmented Generation"?**
- **Retrieval** = finding relevant information
- **Augmented** = adding it to the input
- **Generation** = LLM producing the answer

---

## 1.2 Why RAG Is Needed

### The Problems with Raw LLMs

| Problem | What It Means |
|---------|--------------|
| **Knowledge cutoff** | LLMs don't know recent events |
| **Hallucination** | LLMs confidently make things up |
| **No private data** | LLMs can't access your company docs |
| **Context limits** | You can't paste 10,000 documents into a prompt |
| **Retraining cost** | Updating an LLM with new data costs millions |

### RAG Solves All of This

```
❌ Without RAG:
User: "What are Q3 2024 sales figures?"
LLM: [makes up plausible-sounding numbers]

✅ With RAG:
User: "What are Q3 2024 sales figures?"
System: [retrieves Q3 2024 report from database]
LLM: "According to the Q3 2024 report, sales were $4.2M..."
```

RAG gives LLMs **fresh, accurate, private, and domain-specific knowledge** — without retraining.

---

## 1.3 Fine-tuning vs RAG vs Prompt Engineering

These are three different ways to make an LLM more useful. Understanding the difference is critical.

### The Big Picture

```
Prompt Engineering  →  You give better instructions
Fine-tuning         →  You change the model's behavior
RAG                 →  You give the model better information
```

### Detailed Comparison

| Approach | What Changes | When to Use | Cost | Limitation |
|----------|-------------|-------------|------|------------|
| **Prompt Engineering** | Just the input text | Quick improvements, task framing | Zero | Limited by context window |
| **RAG** | External knowledge is retrieved | Dynamic data, private docs, factual accuracy | Low-Medium | Retrieval quality matters |
| **Fine-tuning** | Model weights | New writing style, specialized vocabulary, task format | High | Doesn't add new facts reliably |

### The Key Insight

> Fine-tuning teaches the model **how to behave**.
> RAG teaches the model **what to say**.

**Common Mistake:** People fine-tune when they should use RAG.
Fine-tuning on facts often causes worse hallucinations — the model "thinks" it knows things it doesn't.

**Pro Tip:** RAG + Prompt Engineering is the most practical starting point for 90% of real applications.

---

## 1.4 Core Concepts

### 1.4.1 Embeddings — How They Work Internally

**Simple Explanation:**
An embedding is a list of numbers that represents the **meaning** of text.

Similar meanings → similar numbers → close in space.

**Step-by-step logic:**

```
Step 1: Take any text (word, sentence, paragraph)
Step 2: Pass it through a neural network (embedding model)
Step 3: The network outputs a vector — a list of 384, 768, or 1536 numbers
Step 4: This vector is a "coordinate" in meaning space
```

**Example:**
```
"dog"   → [0.21, 0.84, -0.32, ... 768 numbers]
"puppy" → [0.19, 0.81, -0.29, ... 768 numbers]  ← very similar
"car"   → [0.91, -0.43, 0.77, ... 768 numbers]  ← very different
```

**Visual intuition:**

```
         (animal axis)
              ↑
    dog • • puppy
              
    cat •
              
              --------→ (vehicle axis)
                   car •
                   truck •
```

Texts with similar meaning cluster together. That's the power of embeddings.

**How the neural network learns this:**
The embedding model is trained on massive text. It learns that "dog" and "puppy" appear in similar contexts, so it assigns them nearby vectors. This is learned — not manually programmed.

---

### 1.4.2 Vector Similarity — How Closeness Is Measured

Once everything is a vector, we need to measure "how similar" two vectors are.

**Three main methods:**

#### Cosine Similarity

Measures the **angle** between two vectors. Ignores magnitude.

```
Cosine Similarity = (A · B) / (|A| × |B|)

Result range: -1 to 1
  1  = identical direction (same meaning)
  0  = perpendicular (unrelated)
 -1  = opposite direction (opposite meaning)
```

**Intuition:** Two arrows pointing in the same direction are similar, regardless of how long they are.

Best for: text similarity (most common in RAG).

#### Dot Product

Measures both **angle and magnitude**.

```
Dot Product = A · B = Σ(Aᵢ × Bᵢ)
```

Best for: when magnitude carries meaning (e.g., some recommendation systems).

#### Euclidean Distance

Measures the straight-line **distance** between points.

```
Distance = √Σ(Aᵢ - Bᵢ)²
```

Best for: image embeddings, spatial data. Less common in NLP RAG.

**Pro Tip:** For RAG, almost always use **cosine similarity**. It's stable, interpretable, and works well with normalized embeddings.

---

### 1.4.3 Retrieval Logic

**Simple Explanation:**
Retrieval is the act of finding the most relevant stored content for a given query.

**The core loop:**

```
1. A user query arrives
2. Convert query to embedding (vector)
3. Compare query vector against all stored document vectors
4. Return Top-K most similar documents
5. Feed those documents as context to the LLM
```

**What "Top-K" means:**
K is how many documents you retrieve. K=3 means "get the 3 most relevant chunks."

More K = more context = better coverage, but:
- More tokens = higher cost
- Too much irrelevant context = worse answers (noise)

Choosing K is a design decision. Usually 3–10 is practical.

**Key Insight:** Retrieval quality is the most important factor in RAG. If the wrong documents are retrieved, the LLM gives wrong answers — even if the LLM itself is excellent.

> "Garbage in, garbage out" applies to RAG retrieval.

---

# SECTION 2: CORE COMPONENTS (LOGIC-FOCUSED)

---

## 2.1 Embedding Generation Pipeline

**The full pipeline from raw text to stored vector:**

```
Raw Documents
     ↓
[Text Extraction]        ← strip HTML, PDF, DOCX → plain text
     ↓
[Cleaning & Normalization] ← remove noise, fix encoding
     ↓
[Chunking]               ← split into smaller pieces
     ↓
[Embedding Model]        ← each chunk → vector
     ↓
[Vector Store]           ← save vectors with metadata
```

**What happens inside the embedding model:**

```
Input text: "The quarterly earnings report shows..."
     ↓
Tokenization: ["The", "quarterly", "earn", "##ings", "report"...]
     ↓
Token Embeddings (each token → vector)
     ↓
Transformer layers (attention mechanism captures relationships)
     ↓
Pooling (combine all token vectors into one chunk vector)
     ↓
Output: [0.12, -0.44, 0.91, ... 768 dims]
```

**Common embedding models:**

| Model | Dims | Best For |
|-------|------|---------|
| `text-embedding-3-small` (OpenAI) | 1536 | General purpose |
| `all-MiniLM-L6-v2` | 384 | Fast, local |
| `bge-large-en` | 1024 | High accuracy |
| `nomic-embed-text` | 768 | Open source, strong |

**Pro Tip:** The embedding model you use during indexing MUST be the same one used at query time. Mixing models breaks everything.

---

## 2.2 Vector Database Internals

**What is a vector database?**
A specialized database designed to store and search vectors (embeddings) efficiently.

Regular databases search by value (WHERE name = 'Alice').
Vector databases search by **meaning** (find me vectors closest to this query vector).

### Indexing Logic

When you insert documents:

```
Insert document →
  1. Compute embedding
  2. Store vector + metadata (doc_id, source, text)
  3. Update the search index
```

The index structure is what makes search fast. Without it, searching 1 million vectors would require comparing your query against all 1 million — very slow.

### ANN Search (Approximate Nearest Neighbor)

**Exact search** — compare against every vector. Accurate but O(n) — slow at scale.

**ANN search** — find "close enough" neighbors very fast. Slight accuracy tradeoff, massive speed gain.

**The most popular ANN algorithm: HNSW**

HNSW (Hierarchical Navigable Small World) builds a layered graph:

```
Layer 2 (sparse): ●---------●---------●
                      \             /
Layer 1 (medium):  ●--●--●------●--●--●
                    \  |  |      |  |  /
Layer 0 (dense):  ●-●-●-●-●--●-●-●-●-●
```

Search starts at the top (sparse), finds the rough neighborhood, then drills down to the dense layer for precision.

**Result:** Search in O(log n) instead of O(n). At 1M vectors, that's roughly 20 comparisons instead of 1,000,000.

### Popular Vector Databases

| Database | Best For | Key Feature |
|----------|---------|------------|
| **Pinecone** | Cloud, production | Fully managed |
| **Weaviate** | Hybrid search | Built-in BM25 |
| **Qdrant** | Performance | Rust-based, fast |
| **Chroma** | Local/dev | Simple, in-memory |
| **pgvector** | PostgreSQL users | SQL + vectors |
| **FAISS** | Research/custom | Facebook's library |

---

## 2.3 Chunking Strategies

**Why chunking matters:**

LLMs have context limits. You can't embed an entire 100-page document as one vector — the embedding would be too diluted.

Chunking = splitting documents into smaller pieces before embedding.

**The core tension:**

```
Too small chunks → miss context, fragmented meaning
Too large chunks → diluted embeddings, slow, expensive
```

### Chunking Strategies Explained

#### 1. Fixed-Size Chunking

Split every N characters or tokens, with overlap.

```
Document: [----500 chars----][----500 chars----][----500 chars----]
With overlap: 
  Chunk 1: chars 0–500
  Chunk 2: chars 400–900   ← 100 char overlap
  Chunk 3: chars 800–1300
```

**Why overlap?** Answers often span chunk boundaries. Overlap ensures context isn't cut off.

**Best for:** Uniform documents (logs, transcripts, articles).

#### 2. Semantic Chunking

Split at natural semantic boundaries (paragraphs, headings, topics).

```
Doc: [Intro paragraph][Heading: Revenue][Revenue table][Heading: Costs]
     ← chunk 1 ──────→←── chunk 2 ──────────────────→←── chunk 3 ──→
```

**Best for:** Structured documents (reports, books, policies).

#### 3. Recursive Character Splitting

Try to split at `\n\n` first, then `\n`, then `.`, then ` `.

```
Priority: paragraph → line → sentence → word
```

This is the most common approach in production — smart but simple.

#### 4. Document-Based Splitting

Use the document's own structure.

```
PDF with sections → one chunk per section
Markdown file → one chunk per ## heading
Code file → one chunk per function
```

**Best for:** Structured formats where structure = meaning.

#### 5. Agentic / Dynamic Chunking

An LLM decides where to split, based on semantic completeness.

**Best for:** Complex documents. **Downside:** Expensive, slow.

### Chunking Decision Guide

```
What type of document?
  ├── Structured (headings, sections) → Semantic or Document-based
  ├── Uniform text (articles, transcripts) → Recursive Character
  ├── Code → Function-level splitting
  └── Unknown/mixed → Recursive Character with overlap
```

**Common Mistake:** Using chunk_size=1000 with no overlap. You'll lose context at chunk boundaries and get retrieval failures on questions that span sections.

---

## 2.4 Indexing Pipeline (Step-by-Step Logic)

The indexing pipeline is the **offline phase** — you do this before users ask questions.

```
┌─────────────────────────────────────────────────────────┐
│                   INDEXING PIPELINE                      │
│                                                          │
│  Raw Docs → Extract → Clean → Chunk → Embed → Store     │
│                                                          │
└─────────────────────────────────────────────────────────┘

Step 1: EXTRACT
  PDF, DOCX, HTML, CSV, etc.
  → Extract plain text
  → Preserve metadata (filename, page, date, author)

Step 2: CLEAN
  → Remove headers/footers
  → Fix encoding issues
  → Remove duplicate content
  → Normalize whitespace

Step 3: CHUNK
  → Apply chosen chunking strategy
  → Assign chunk ID + parent doc metadata

Step 4: EMBED
  → Pass each chunk through embedding model
  → Get vector for each chunk
  → Batch processing for efficiency

Step 5: STORE
  → Insert (vector, chunk_text, metadata) into vector DB
  → Update ANN index
```

**Metadata is critical.** Always store:
- `source` (filename/URL)
- `chunk_index` (position in doc)
- `created_at` (for freshness filtering)
- `doc_type` (for filtering by category)

**Pro Tip:** Store the original chunk text alongside the vector. You'll need it to inject into the LLM prompt later — you can't reconstruct text from a vector.

---

## 2.5 Query Pipeline (Step-by-Step Reasoning)

The query pipeline is the **online phase** — runs every time a user asks a question.

```
┌─────────────────────────────────────────────────────────────────┐
│                      QUERY PIPELINE                              │
│                                                                  │
│  User Query                                                      │
│      ↓                                                           │
│  [Query Processing]  ← rewrite, expand, classify               │
│      ↓                                                           │
│  [Embedding]         ← query → vector                          │
│      ↓                                                           │
│  [Vector Search]     ← ANN search against index                │
│      ↓                                                           │
│  [Filtering]         ← metadata filters (date, source, type)   │
│      ↓                                                           │
│  [Re-ranking]        ← reorder by relevance                    │
│      ↓                                                           │
│  [Context Assembly]  ← format top-K chunks into prompt         │
│      ↓                                                           │
│  [LLM Generation]    ← model generates answer                  │
│      ↓                                                           │
│  Response                                                        │
└─────────────────────────────────────────────────────────────────┘
```

**Reasoning at each step:**

| Step | Why It Matters |
|------|---------------|
| Query Processing | Raw queries are often ambiguous. Rewriting improves retrieval. |
| Embedding | Query and docs must use the same embedding space. |
| Vector Search | Fast ANN returns candidates. Not final ranking. |
| Filtering | Remove irrelevant sources before ranking. Saves cost. |
| Re-ranking | ANN returns approximate matches. Re-ranking adds precision. |
| Context Assembly | Order and format of context affects LLM answer quality. |
| LLM Generation | LLM synthesizes an answer from context + query. |

**Key Insight:** The query pipeline is a chain. A failure at step 2 propagates all the way to the final answer. Each step must be designed carefully.

---

# SECTION 3: RAG ARCHITECTURE

---

## 3.1 End-to-End System Architecture

A full RAG system has two parallel systems: the **indexing system** (offline) and the **serving system** (online).

```
╔══════════════════════════════════════════════════════════════╗
║                    OFFLINE: INDEXING SYSTEM                   ║
║                                                               ║
║  [Document Sources]                                           ║
║   PDFs  CSVs  HTML  APIs  Databases                          ║
║        ↓                                                      ║
║  [Document Loader]    ← connectors for each source type      ║
║        ↓                                                      ║
║  [Text Extractor]     ← extract clean plain text             ║
║        ↓                                                      ║
║  [Chunker]            ← split into chunks                    ║
║        ↓                                                      ║
║  [Embedding Model]    ← chunk → vector                       ║
║        ↓                                                      ║
║  [Vector Store]       ← Pinecone, Qdrant, Weaviate           ║
╚══════════════════════════════════════════════════════════════╝

                         ↕ (shared index)

╔══════════════════════════════════════════════════════════════╗
║                   ONLINE: SERVING SYSTEM                      ║
║                                                               ║
║  [User Query]                                                 ║
║        ↓                                                      ║
║  [Query Processor]    ← rewrite / expand / classify          ║
║        ↓                                                      ║
║  [Embedding Model]    ← same model as indexing!              ║
║        ↓                                                      ║
║  [Retriever]          ← ANN search → Top-K candidates        ║
║        ↓                                                      ║
║  [Re-ranker]          ← optional precision boost             ║
║        ↓                                                      ║
║  [Prompt Builder]     ← inject context into prompt template  ║
║        ↓                                                      ║
║  [LLM]                ← generate answer                      ║
║        ↓                                                      ║
║  [Response]           ← with citations / sources             ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 3.2 Data Ingestion Flow

This is how documents get into the system.

```
Source Document (e.g., employee_handbook.pdf)
         │
         ▼
┌─────────────────┐
│  File Loader    │  ← reads binary file
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Text Extractor  │  ← PDF parser, HTML stripper, DOCX reader
└────────┬────────┘
         │  "The company was founded in 2010. Our mission is..."
         ▼
┌─────────────────┐
│   Chunker       │  ← splits into 300-500 token pieces with overlap
└────────┬────────┘
         │  Chunk 1: "The company was founded in 2010..."
         │  Chunk 2: "Our mission is to provide..."
         │  Chunk 3: "Employee benefits include..."
         ▼
┌─────────────────┐
│ Embedding Model │  ← each chunk → 768-dim vector
└────────┬────────┘
         │  Chunk 1 → [0.21, -0.44, 0.91, ...]
         │  Chunk 2 → [0.55, 0.12, -0.33, ...]
         ▼
┌──────────────────────────────────────────┐
│           Vector Store                    │
│  id: "chunk_001"                          │
│  vector: [0.21, -0.44, 0.91, ...]        │
│  text: "The company was founded..."      │
│  metadata: {source: "handbook.pdf",       │
│             page: 1, date: "2024-01-15"} │
└──────────────────────────────────────────┘
```

---

## 3.3 Retrieval Flow

This runs every time a user asks a question.

```
User: "What are the employee vacation policies?"
         │
         ▼
┌──────────────────┐
│  Query Processor │  ← optionally rewrite/expand query
└────────┬─────────┘
         │  Query: "vacation policies for employees"
         ▼
┌──────────────────┐
│ Embedding Model  │  ← same model used during indexing
└────────┬─────────┘
         │  Query vector: [0.48, -0.22, 0.87, ...]
         ▼
┌──────────────────────────────────┐
│        Vector Store Search        │
│  ANN search: find top-5 closest  │
│  to query vector                  │
└────────┬─────────────────────────┘
         │
         │  Results:
         │  Score 0.92 → Chunk "Vacation days: employees get 15 days..."
         │  Score 0.88 → Chunk "Annual leave policy states that..."
         │  Score 0.85 → Chunk "HR policy: time off requests must..."
         │  Score 0.79 → Chunk "Benefits overview: health, dental..."
         │  Score 0.71 → Chunk "Company founded 2010, now 500 employees"
         ▼
┌──────────────────┐
│   Re-ranker      │  ← re-scores with cross-encoder for precision
└────────┬─────────┘
         │  Final top-3: chunks 1, 2, 3
         ▼
┌──────────────────┐
│  Prompt Builder  │
└──────────────────┘
```

---

## 3.4 Generation Flow

After retrieval, the LLM uses the retrieved context to answer.

```
┌─────────────────────────────────────────────────────────────┐
│                      PROMPT STRUCTURE                        │
│                                                              │
│  [System Prompt]                                             │
│  You are a helpful assistant. Answer ONLY using the         │
│  provided context. If unsure, say so.                        │
│                                                              │
│  [Retrieved Context]                                         │
│  --- Document 1 (Source: handbook.pdf, Page 4) ---          │
│  Employees receive 15 days of paid vacation per year...     │
│                                                              │
│  --- Document 2 (Source: hr_policy.pdf, Page 12) ---        │
│  Vacation requests must be submitted 2 weeks in advance...  │
│                                                              │
│  --- Document 3 (Source: benefits.pdf, Page 2) ---          │
│  Annual leave accumulates at 1.25 days per month...         │
│                                                              │
│  [User Question]                                             │
│  What are the employee vacation policies?                   │
│                                                              │
│  [LLM Answer]                                                │
│  Employees receive 15 days of paid vacation per year,       │
│  accumulating at 1.25 days/month. Requests must be          │
│  submitted at least 2 weeks in advance.                      │
│                                                              │
│  Sources: handbook.pdf (p.4), hr_policy.pdf (p.12)          │
└─────────────────────────────────────────────────────────────┘
```

**Key design decisions in the generation flow:**

| Decision | Options | Impact |
|----------|---------|--------|
| System prompt instruction | "Use only context" vs "Use context + knowledge" | Hallucination risk |
| Context ordering | Best-first vs worst-first vs original order | Answer quality ("lost in the middle" problem) |
| Source citation | Include vs exclude | Trustworthiness |
| Fallback behavior | "I don't know" vs best guess | Reliability |

**Lost in the Middle Problem:**
Research shows LLMs pay more attention to content at the **beginning and end** of the context. Important chunks placed in the middle get ignored. Solution: put the most relevant chunk first.

---

# SECTION 4: RETRIEVAL TECHNIQUES

---

## 4.1 Dense vs Sparse Retrieval

There are two fundamentally different ways to find relevant documents.

### Dense Retrieval (Semantic)

Uses neural embeddings. Finds documents with **similar meaning**.

```
Query: "car problems"
Matches: "vehicle maintenance issues" ✅ (different words, same meaning)
```

**How it works internally:**
1. Both query and document are embedded into vectors
2. Similarity is computed (cosine similarity)
3. Top-K closest vectors are returned

**Strengths:** Handles paraphrasing, synonyms, conceptual similarity.
**Weakness:** Can miss exact keyword matches. Expensive (needs GPU for large models).

---

### Sparse Retrieval (Lexical)

Uses exact word matching. Classic information retrieval.

```
Query: "car problems"
Matches: "car problems reported in 2023" ✅ (exact keyword overlap)
Not matched: "vehicle maintenance issues" ❌ (no keyword overlap)
```

The most powerful sparse method is **BM25**.

---

## 4.2 BM25 — Intuition and Formula

**BM25 = Best Match 25** — a refined version of TF-IDF.

**The Core Idea:**
Score a document by how many query terms it contains, but with smart corrections for:
- Term frequency (appearing 100× isn't 100× better)
- Document length (short docs shouldn't have an unfair advantage)

**The Formula:**

```
BM25(Q, D) = Σ IDF(qᵢ) × [ TF(qᵢ, D) × (k₁ + 1) ]
                              ─────────────────────────
                              TF(qᵢ, D) + k₁ × (1 - b + b × |D|/avgDL)
```

**Breaking it down:**

| Part | Meaning |
|------|---------|
| `IDF(qᵢ)` | Inverse Document Frequency — rare words score higher |
| `TF(qᵢ, D)` | How often the term appears in this document |
| `k₁` | Controls TF saturation (usually 1.2–2.0) |
| `b` | Controls length normalization (usually 0.75) |
| `|D| / avgDL` | Ratio of doc length to average doc length |

**Intuition example:**

```
Query: "database performance"

Doc A (short, 50 words): "database performance tuning is critical"
Doc B (long, 5000 words): "database is used for performance in many contexts..."

Without length normalization → Doc B wins (just because it's long)
With BM25 length normalization → Doc A wins (denser relevant content)
```

**Why BM25 is still relevant in 2024:**
- Handles rare technical terms, product names, error codes perfectly
- Dense retrieval often fails on exact identifiers ("Error 0x80004005")
- BM25 is deterministic, fast, and needs no GPU

---

## 4.3 Hybrid Search — Why It Works Better

**Simple Explanation:**
Combine dense (semantic) and sparse (keyword) retrieval and merge their results.

```
                    User Query
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
   Dense Retrieval              Sparse (BM25)
   (embedding search)           (keyword search)
          │                           │
          ▼                           ▼
   Top-K semantic matches      Top-K keyword matches
          │                           │
          └─────────────┬─────────────┘
                        ▼
              [Score Fusion (RRF)]
                        ▼
               Final ranked results
```

**Reciprocal Rank Fusion (RRF):**
A simple, effective way to merge two ranked lists.

```
RRF_score(doc) = Σ 1 / (rank_in_list + k)
```

A document ranked #1 in both lists gets a higher combined score than one ranked #1 in only one list.

**Why hybrid works better than either alone:**

| Scenario | Dense Only | Sparse Only | Hybrid |
|----------|-----------|-------------|--------|
| "What is machine learning?" | ✅ | ✅ | ✅ |
| "Python AttributeError 'NoneType'" | ❌ | ✅ | ✅ |
| "explain neural networks simply" | ✅ | ❌ | ✅ |
| "GPT-4 API rate limit 429 error" | ❌ | ✅ | ✅ |

Hybrid is almost always better. Use it as your default.

---

## 4.4 Re-ranking — Cross-Encoder Logic

**The Problem:**
ANN search returns approximate results. The top-10 from vector search isn't perfectly ranked by relevance.

**The Solution: Re-ranking**

Use a more powerful (but slower) model to re-score the candidates.

```
ANN Search returns 20 candidates (fast but approximate)
         │
         ▼
Cross-Encoder re-ranks the 20 candidates (slow but precise)
         │
         ▼
Return top-5 for context injection
```

**How a Cross-Encoder works:**

A bi-encoder (normal embedding model) encodes query and document **separately** and compares vectors.

A cross-encoder takes the **query + document together** as a single input and outputs a relevance score.

```
Bi-encoder:   embed(query) vs embed(doc)   → score  [fast]
Cross-encoder: encode(query + doc together) → score  [slow, accurate]
```

Cross-encoders understand full interaction between query and document. They can catch subtle relevance signals bi-encoders miss.

**Trade-off:**
- Re-ranking 1000 candidates is expensive (too slow for production)
- Re-ranking 20–50 candidates is practical

**Common Pipeline:**

```
Vector search → top 50 candidates
Re-ranker     → re-scores all 50
Final output  → top 5 after re-ranking
```

---

## 4.5 Multi-Query Retrieval — Query Expansion Logic

**The Problem:**
A single query may miss relevant documents if they use different terminology.

**Example:**
```
Query: "How do I reduce server response time?"
Misses: docs about "latency optimization", "API performance", "caching strategies"
```

**The Solution: Generate multiple queries and retrieve for all of them.**

```
Original Query: "How do I reduce server response time?"
         │
         ▼
[LLM Query Expander]
         │
         ▼
Generated queries:
  1. "server latency reduction techniques"
  2. "API response time optimization"
  3. "web server performance tuning"
  4. "caching strategies for faster responses"
         │
         ▼
Run retrieval for EACH query
         │
         ▼
Deduplicate results
         │
         ▼
Combined unique top-K documents
```

**Why this works:**
Different phrasings retrieve different (but relevant) documents. The union covers more ground than a single query.

**Downside:** 4× the queries = 4× the cost and latency.

**When to use it:** Complex or ambiguous questions, research applications, low-latency-tolerance tasks.

---

## 4.6 Context Compression — How Models Filter Useful Data

**The Problem:**
Retrieved chunks often contain both relevant and irrelevant text. Sending 5 large chunks to the LLM adds noise and cost.

**The Solution: Compress or filter the retrieved content before sending it.**

```
Retrieved Chunk (full):
"The company was founded in 1998. Revenue grew 15% last year. 
The CEO is James Wilson. Employee benefits include health insurance, 
dental, and 15 days vacation. The office is in San Francisco. 
Stock ticker: COMP. Vacation requests must be filed 2 weeks ahead."

Query: "What are the vacation policies?"

After Context Compression:
"15 days vacation. Vacation requests must be filed 2 weeks ahead."
```

**Two ways to do this:**

#### 1. LLM-based Compression
Ask an LLM: "Extract only the parts relevant to this question."
- Accurate
- Adds LLM latency + cost

#### 2. Sentence-level Filtering
Split chunk into sentences, embed each, keep only those semantically similar to query.
- Fast
- Less accurate for complex reasoning

**When to use:** Long documents, high token costs, multi-document retrieval where each chunk is large.

---

## Interview Questions — Sections 1–4

1. What is the difference between fine-tuning and RAG? When would you choose each?
2. Why do we chunk documents before embedding them? What are the trade-offs of chunk size?
3. Explain BM25. How does it differ from simple term frequency matching?
4. Why is hybrid search better than dense-only retrieval?
5. What is the difference between a bi-encoder and a cross-encoder? Why can't we use a cross-encoder for the initial search?
6. What is the "lost in the middle" problem and how do you address it?
7. Why must you use the same embedding model for indexing and querying?
8. What metadata should you always store with your vector embeddings?

---

## Exercises — Sections 1–4

1. **Trace a query:** Take the query "What is the refund policy?" and trace it step by step through the entire RAG pipeline — from query to final answer.
2. **Chunking experiment:** Take one document and chunk it with three strategies (fixed-size, semantic, document-based). Which chunks look most meaningful?
3. **BM25 intuition:** Without code, explain why the query "Python NoneType error" would return different results in BM25 vs dense retrieval.
4. **Design a pipeline:** Design a hybrid retrieval system for a codebase assistant. What chunking strategy would you use? What retrieval method?