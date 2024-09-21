import matplotlib.pyplot as plt

# Redraw the flowchart with the requested layout: main.py, gst_data, cme_data, and services.py on the outer positions

fig, ax = plt.subplots(figsize=(10, 6))

# Define positions for the blocks (rearranged to have outer placements for the requested files)
positions = {
    "main.py": (0.5, 0.9),
    "cme_data.ipynb": (0.1, 0.6),
    "gst_data.ipynb": (0.9, 0.6),
    "merge_data.ipynb": (0.5, 0.5),
    "services.py": (0.5, 0.1),
}

# Draw the blocks
for filename, pos in positions.items():
    ax.text(
        pos[0],
        pos[1],
        filename,
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#DDDDDD"),
    )

# Draw arrows between the blocks to represent file connections
arrow_params = dict(facecolor="black", arrowstyle="->")

# Arrows from main.py to the other scripts
ax.annotate(
    "",
    xy=positions["cme_data.ipynb"],
    xytext=positions["main.py"],
    arrowprops=arrow_params,
)
ax.annotate(
    "",
    xy=positions["gst_data.ipynb"],
    xytext=positions["main.py"],
    arrowprops=arrow_params,
)
ax.annotate(
    "",
    xy=positions["merge_data.ipynb"],
    xytext=positions["main.py"],
    arrowprops=arrow_params,
)

# Arrows showing dependency of cme_data, gst_data, and merge_data on services.py
ax.annotate(
    "",
    xy=positions["services.py"],
    xytext=positions["cme_data.ipynb"],
    arrowprops=arrow_params,
)
ax.annotate(
    "",
    xy=positions["services.py"],
    xytext=positions["gst_data.ipynb"],
    arrowprops=arrow_params,
)
ax.annotate(
    "",
    xy=positions["services.py"],
    xytext=positions["merge_data.ipynb"],
    arrowprops=arrow_params,
)

# Set limits, hide axes, and show
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Display the flowchart
plt.show()
