import './App.css';
import { useState } from 'react';

function App() {

    const corrections = {
        "realy": "really",
        "teh": "the",
        "exmaple": "example",
        "wierd": "weird",
        "spce": "space"
    };

    const [text, setText] = useState("");

    const handleUserType = (e) => {
        const input = e.target.value;

        const words = input.split(" ");
        if (words.length > 1) {
            const lastWord = words[words.length - 2];

            if (corrections[lastWord]) {
                words[words.length - 2] = corrections[lastWord];
                const correctedText = words.join(" ");
                setText(correctedText);
                return;
            }
        }
        setText(input);
    };

    return (
    <div className="container">
        <h3>Autocorrect</h3>
       <textarea
            data-testid="textarea"
            value={text}
            onChange={handleUserType}
            rows="10"
            cols="50"
            placeholder="Write something here..."
       />
    </div>
  );
}

export default App;
