import { useState } from "react"

export default function ChatInput({ onSend, disabled }) {
  const [value, setValue] = useState("")

  function handleSubmit(e) {
    e.preventDefault()
    const trimmed = value.trim()
    if (!trimmed || disabled) return
    onSend(trimmed)
    setValue("")
  }

  return (
    <form onSubmit={handleSubmit} className="flex gap-3">
      <input
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder="Ask a question about your documents..."
        className="flex-1 rounded-2xl border border-slate-700 bg-slate-900 px-4 py-3 text-sm outline-none placeholder:text-slate-500 focus:border-slate-500"
      />
      <button
        type="submit"
        disabled={disabled}
        className="rounded-2xl bg-slate-100 px-5 py-3 text-sm font-medium text-slate-900 disabled:cursor-not-allowed disabled:opacity-50"
      >
        Send
      </button>
    </form>
  )
}