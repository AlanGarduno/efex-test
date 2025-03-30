import React from "react";
import { render, fireEvent, screen } from "@testing-library/react";
import App from "./App";

describe("Autocorrect functionality", () => {
  it("corrects a misspelled word after typing a space", () => {
    render(<App />);

    const textarea = screen.getByTestId("textarea");

    fireEvent.change(textarea, { target: { value: "realy " } });

    expect(textarea.value).toBe("really ");
  });

  it("does not change text when word is correct", () => {
    // Render the App component
    render(<App />);

    const textarea = screen.getByTestId("textarea");

    fireEvent.change(textarea, { target: { value: "really " } });

    expect(textarea.value).toBe("really ");
  });

  it("corrects multiple misspelled words properly", () => {
    render(<App />);

    const textarea = screen.getByTestId("textarea");

    fireEvent.change(textarea, { target: { value: "realy " } });
    expect(textarea.value).toBe("really ");
    fireEvent.change(textarea, { target: { value: "really teh " } });
    expect(textarea.value).toBe("really the ");
    fireEvent.change(textarea, { target: { value: "really the exmaple " } });

    expect(textarea.value).toBe("really the example ");
  });

  it("does not autocorrect until a space is typed", () => {
    render(<App />);

    const textarea = screen.getByTestId("textarea");

    fireEvent.change(textarea, { target: { value: "realy" } });

    expect(textarea.value).toBe("realy");
  });

});
