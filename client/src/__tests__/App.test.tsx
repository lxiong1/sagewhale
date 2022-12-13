import {render, screen} from '@testing-library/react'
import { App } from "../App"

test("Should render color mode button", () => {
  render(<App />)

  expect(screen.getByRole("button", { name: "Switch to dark mode" })).toBeInTheDocument()
})
