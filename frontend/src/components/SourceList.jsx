export default function SourceList({ sources }) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950/60 p-3">
      <div className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-400">
        Sources
      </div>

      <div className="space-y-2">
        {sources.map((source, index) => (
          <div
            key={`${source.id || source.source || index}`}
            className="rounded-lg border border-slate-800 bg-slate-900 px-3 py-2 text-xs text-slate-300"
          >
            <div><span className="text-slate-500">file:</span> {source.filename || "-"}</div>
            <div><span className="text-slate-500">namespace:</span> {source.namespace || "-"}</div>
            <div><span className="text-slate-500">chunk:</span> {source.chunk_index ?? "-"}</div>
          </div>
        ))}
      </div>
    </div>
  )
}