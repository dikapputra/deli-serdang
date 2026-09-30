from pathlib import Path
from urllib.request import Request, urlopen
base=Path('/Users/dikapranandaputra/dokumen/jejak-deli-serdang/assets')
items={
'hamparan-tempo-dulu.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ae/Hamparan_perak_tempo_dulu.jpg/960px-Hamparan_perak_tempo_dulu.jpg',
'tandem-heritage.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6a/Administrateurswoning_op_tabaksonderneming_Tandem%2C_vermoedelijk_in_Langkat%2C_KITLV_93295.tiff/lossy-page1-960px-Administrateurswoning_op_tabaksonderneming_Tandem%2C_vermoedelijk_in_Langkat%2C_KITLV_93295.tiff.jpg',
}
for name,url in items.items():
    data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read(); (base/name).write_bytes(data); print(name,len(data))
