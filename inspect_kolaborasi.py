with open('kolaborasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_tag = 'id="kolaborasiListContainer"'
pos1 = text.find(start_tag)
pos2 = text.find('</section>', pos1)
cards_block = text[pos1:pos2]
print(f"Cards block length: {len(cards_block)}")

# Let's count cards
card_splits = cards_block.split('<div class="card"')
print(f"Number of card elements: {len(card_splits) - 1}")
