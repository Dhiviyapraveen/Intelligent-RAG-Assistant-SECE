import "./Message.css";

import SourceCard from "../SourceCard/SourceCard";

function Message({ message }) {
  return (
    <div
      className={
        message.type === "user"
          ? "message user-message"
          : "message bot-message"
      }
    >
      <div className="message-header">
        {message.type === "user"
          ? "👤 You"
          : "🤖 Assistant"}
      </div>

      <div className="message-body">
        {message.text}
      </div>

      {message.type === "bot" &&
        message.sources &&
        message.sources.length > 0 && (
          <div className="sources">

            <h4>Sources</h4>

            {message.sources.map((source, index) => (
              <SourceCard
                key={index}
                source={source}
              />
            ))}

          </div>
        )}

    </div>
  );
}

export default Message;