# LLM Wiki vs Traditional RAG

Two ways to give an LLM memory over your knowledge, contrasted in [[andrej-karpathy-llm-wiki-obsidian]].

- **[[llm-wiki-pattern|LLM Wiki]]** (this vault): interlinked, human-readable markdown the LLM writes and maintains; explicit cross-references; improves with curation; you can read/audit it directly.
- **Vector [[rag|RAG]]**: opaque embedding similarity search over chunked text; scales to huge corpora but is a black box.

Rule of thumb: wiki for a curated, navigable knowledge base you also read; vector RAG for large-scale multimodal retrieval ([[google-rag-gemini-embeddings-2]]).
