# UI Changes and Operations Performed

I have redesigned the `calculator1.py` application to improve its aesthetic and simplicity. Below is a list of all operations performed:

## Iteration 2: Image Replication

1. **Color Palette Update**:
   - Matches the provided visual exactly:
     - **Window Background**: Medium Blue (`#4b76a8`).
     - **Display Screen**: Lighter Gray-Blue (`#6a8eb3`) with Bright Yellow text (`#ffe345`).
     - **Number Buttons**: Light Periwinkle (`#cdd5ec`) with Dark Blue text (`#2b3a67`).
     - **Operator Buttons**: Crisp White (`#ffffff`) with Dark Blue text (`#2b3a67`).
     - **Clear Button (C)**: Highlighted Yellow (`#ffca28`).

2. **Button Grid Layout Changes**:
   - Recreated the 5x4 grid exactly as shown in the image.
   - The layout is now:
     - `C`, `%`, `÷`, `x`
     - `7`, `8`, `9`, `-`
     - `4`, `5`, `6`, `+`
     - `1`, `2`, `3`, `=` (Spans vertically across two rows)
     - `0`, `00`, `.` (Bottom row)
   - Made the `=` button span both Row 4 and Row 5 using `rowspan=2`.

3. **Symbol Parsing (`eval`) Updates**:
   - Replaced custom layout symbols `÷` and `x` internally with Python operators `/` and `*` before parsing the math, ensuring the calculator remains functional.

---

## Iteration 1: Dark Mode

1. **Color Theme Upgrade**:
   - Replaced the bright "powder blue" and "cyan" color scheme with a sleek modern dark mode (background: `#202020`).
   - Assigned distinct colors for different button categories:
     - **Numbers**: Dark Gray (`#333333`) with white text.
     - **Operations (+, -, *, /, =)**: Vibrant Orange (`#FF9500`) to highlight primary actions.
     - **Functions (C, M, parentheses)**: Light Gray (`#A5A5A5`) with black text.
     
2. **Typography and Spacing Improvements**:
   - Changed the default bold Arial font to cleaner `Helvetica`.
   - Increased the size of the main display (`Entry` widget) for better readability.
   - Removed the bulky `bd=8` (border width) to adopt a `FLAT` button relief, which creates a cleaner, minimalist aesthetic.
   - Adjusted `padx` and `pady` around buttons to `1`, creating sleek thin grid lines between the buttons.

3. **Layout & UX Tweaks**:
   - Added `cal.geometry("350x500")` to give the calculator an initial, well-proportioned rectangular size.
   - Re-ordered the number buttons `4, 5, 6` and `1, 2, 3` to match a standard calculator layout (they were previously placed backwards like `6, 5, 4` and `3, 2, 1`).
   - Added grid weights (`grid_rowconfigure` / `grid_columnconfigure`) and `sticky="nsew"` to all UI elements so that the application properly scales and resizes if the user changes the window size.

4. **Error Handling (Bug fix)**:
   - Wrapped the `eval()` function in `btnEqualsInput()` with a `try-except` block to prevent the application from crashing when an invalid mathematical expression is entered (e.g., `5*/5`), displaying "Error" instead.
