import axios from "axios";
import { useState } from "react";

export default function Upload() {

  const [file, setFile] = useState(null);

  const uploadFile = () => {
    const form = new FormData();
    form.append("file", file);

    axios.post("http://127.0.0.1:8000/api/upload/", form)
      .then(() => {
        alert("CSV Uploaded Successfully");
        window.location.reload();
      })
      .catch(() => alert("Upload Failed"));
  };

  return (
    <div>
      <input type="file"
        onChange={e => setFile(e.target.files[0])} />

      <button onClick={uploadFile}>
        Upload CSV
      </button>
    </div>
  );
}
