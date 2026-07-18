import "./ChatInput.css";

function ChatInput({
  question,
  setQuestion,
  handleSend,
}) {
  return (
    <div className="chat-input-container">

      <input
        type="text"
        placeholder="Ask anything about SECE..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSend();
          }
        }}
      />

      <button onClick={handleSend}>
        Send
      </button>

    </div>
  );
}

export default ChatInput;