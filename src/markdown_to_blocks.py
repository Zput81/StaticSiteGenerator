def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    raw_blocks = markdown.split("\n\n")
    blocks = []
    for block in raw_blocks:
        if block.strip():
            lines = [line.strip() for line in block.split("\n")]
            blocks.append("\n".join(lines))
    return blocks
