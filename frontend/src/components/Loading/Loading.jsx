import "./Loading.css";

function Loading() {
  return (
    <div className="loading-container">
      <div className="loading-spinner"></div>
      <p>Generating response...</p>
    </div>
  );
}

export default Loading;