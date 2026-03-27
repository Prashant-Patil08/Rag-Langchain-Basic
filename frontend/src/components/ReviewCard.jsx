export default function ReviewCard({
  toolName,
  title,
  to,
  subject,
  body,
  onApprove,
  onEdit,
  onReject
}) {
  return (
    <div className="overflow-hidden rounded-2xl border border-slate-700 bg-slate-950">
      <div className="flex items-center justify-between border-b border-slate-800 px-4 py-3">
        <div className="text-sm font-semibold text-slate-100">{title}</div>
        <div className="rounded-full bg-amber-500/20 px-3 py-1 text-xs font-medium text-amber-300">
          Awaiting Approval
        </div>
      </div>

      <div className="p-4">
        <div className="rounded-2xl bg-slate-800 p-4">
          <div className="mb-1 text-sm font-semibold text-slate-100">{toolName}</div>
          <div className="mb-4 text-sm text-slate-400">Review action before sending</div>

          <div className="space-y-3 text-sm">
            <div>
              <div className="text-xs uppercase tracking-wide text-slate-500">To</div>
              <div className="mt-1 text-slate-100">{to}</div>
            </div>

            <div>
              <div className="text-xs uppercase tracking-wide text-slate-500">Subject</div>
              <div className="mt-1 text-slate-100">{subject}</div>
            </div>

            <div>
              <div className="text-xs uppercase tracking-wide text-slate-500">Body</div>
              <div className="mt-1 text-slate-100">{body}</div>
            </div>
          </div>
        </div>

        <div className="mt-4 flex flex-wrap gap-3">
          <button
            onClick={onApprove}
            className="rounded-xl bg-emerald-500 px-4 py-2 text-sm font-medium text-white"
          >
            Approve
          </button>
          <button
            onClick={onEdit}
            className="rounded-xl border border-slate-700 bg-slate-900 px-4 py-2 text-sm font-medium text-slate-100"
          >
            Edit
          </button>
          <button
            onClick={onReject}
            className="rounded-xl border border-red-500/40 bg-slate-900 px-4 py-2 text-sm font-medium text-red-400"
          >
            Reject
          </button>
        </div>
      </div>
    </div>
  )
}