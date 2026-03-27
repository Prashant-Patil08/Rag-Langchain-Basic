import { useState } from "react"
import ChatMessage from "./components/ChatMessage"
import ChatInput from "./components/ChatInput"

const API_BASE = "http://127.0.0.1:8000"

export default function App() {
  const [messages, setMessages] = useState([
    {
      id: crypto.randomUUID(),
      role: "assistant",
      content: "Hi — ask me anything about your indexed documents.",
      sources: []
    }
  ])
  const [loading, setLoading] = useState(false)

  async function handleSend(text) {
    const userMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: text
    }

    setMessages((prev) => [...prev, userMessage])
    setLoading(true)

    try {
      const res = await fetch(`${API_BASE}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message: text,
          filters: null,
          k: 5
        })
      })

      if (!res.ok) {
        throw new Error(`HTTP ${res.status}`)
      }

      const data = await res.json()

      const assistantMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: data.answer,
        sources: data.sources || []
      }

      setMessages((prev) => [...prev, assistantMessage])
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "assistant",
          content: `Error: ${err.message}`,
          sources: []
        }
      ])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto flex h-screen max-w-6xl flex-col">
        <header className="border-b border-slate-800 px-6 py-4">
          <h1 className="text-xl font-semibold">LangChain RAG Chat</h1>
          <p className="mt-1 text-sm text-slate-400">
            Gemini extracted docs · LangChain retrieval · FastAPI backend
          </p>
        </header>

        <main className="flex-1 overflow-y-auto px-4 py-6 md:px-6">
          <div className="mx-auto flex max-w-4xl flex-col gap-4">
            {messages.map((msg) => (
              <ChatMessage key={msg.id} message={msg} />
            ))}

            {loading && (
              <div className="max-w-[80%] rounded-2xl border border-slate-800 bg-slate-900 px-4 py-3 text-sm text-slate-300">
                Thinking...
              </div>
            )}
          </div>
        </main>

        <footer className="border-t border-slate-800 px-4 py-4 md:px-6">
          <div className="mx-auto max-w-4xl">
            <ChatInput onSend={handleSend} disabled={loading} />
          </div>
        </footer>
      </div>
    </div>
  )
}