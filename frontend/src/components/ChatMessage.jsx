import SourceList from "./SourceList"
import ReviewCard from "./ReviewCard"

export default function ChatMessage({ message }) {
  const isUser = message.role === "user"

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={[
          "max-w-[85%] rounded-2xl px-4 py-3 shadow-sm",
          isUser
            ? "bg-blue-600 text-white"
            : "border border-slate-800 bg-slate-900 text-slate-100"
        ].join(" ")}
      >
        <div className="whitespace-pre-wrap text-sm leading-6">
          {message.content}
        </div>

        {!isUser && message.sources?.length > 0 && (
          <div className="mt-4">
            <SourceList sources={message.sources} />
          </div>
        )}

        {!isUser && message.showReviewCard && (
          <div className="mt-4">
            <ReviewCard
              toolName="send_email"
              title="Review Required"
              to="team@acme.com"
              subject="Q4 Results"
              body="Revenue grew 15% this quarter"
              onApprove={() => console.log("approved")}
              onEdit={() => console.log("edit")}
              onReject={() => console.log("reject")}
            />
          </div>
        )}
      </div>
    </div>
  )
}