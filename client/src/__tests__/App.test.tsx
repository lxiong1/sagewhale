import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { App } from "../App";

test("Should switch color mode on click", async () => {
  render(<App />);
  const user = userEvent.setup();

  expect(
    screen.getByRole("button", { name: "Switch to dark mode" })
  ).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "Switch to dark mode" }));

  expect(
    screen.getByRole("button", { name: "Switch to light mode" })
  ).toBeInTheDocument();
});
