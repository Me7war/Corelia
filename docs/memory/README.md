
<div align="center">
	<h1>🧠 Memory System</h1>
	<img src="https://img.icons8.com/color/96/database.png" alt="Memory"/>
</div>

Corelia uses a hybrid memory system:
- **Long-term**: Qdrant/Weaviate vector database for persistent context.
- **Short-term**: In-memory cache for fast, ephemeral state.

## Usage
- Agents store and retrieve context via `remember()` and vector search.
- Configure Qdrant/Weaviate in `.env`.

See `memory/vectordb.py` and `memory/cache.py` for details.