import "./SourceCard.css";

function SourceCard({ source }) {
  return (
    <div className="source-card">

      <h4>{source.title}</h4>

      <a
        href={source.url}
        target="_blank"
        rel="noreferrer"
      >
        Visit Source
      </a>

    </div>
  );
}

export default SourceCard;