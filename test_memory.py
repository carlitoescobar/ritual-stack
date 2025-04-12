from memory.memory_manager import MemoryManager

mem = MemoryManager()
mem.add_memory("Oracle came online today.", {"tag": "milestone"})
mem.add_memory("Installed Whisper.cpp and Piper.")
print(mem.search_memory("oracle"))
