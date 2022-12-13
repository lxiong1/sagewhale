import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import TypeWriterEffect from "../../components/TypeWriterEffect";

test("Should render type writer effect", async () => {
  render(<TypeWriterEffect />);

  expect(screen.getByTestId("typewriter-wrapper")).toBeInTheDocument();
});
