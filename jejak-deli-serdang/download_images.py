from pathlib import Path
from urllib.request import Request, urlopen

base=Path('/Users/dikapranandaputra/dokumen/jejak-deli-serdang/assets')
base.mkdir(parents=True, exist_ok=True)
items={
'museum-exterior.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a7/Museum_Deli_Serdang_2022_Bennylin_04.jpg/960px-Museum_Deli_Serdang_2022_Bennylin_04.jpg',
'museum-gallery.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/67/Museum_Deli_Serdang_2022_Bennylin_05.jpg/960px-Museum_Deli_Serdang_2022_Bennylin_05.jpg',
'museum-collection.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/92/Museum_Deli_Serdang_2022_Bennylin_14.jpg/960px-Museum_Deli_Serdang_2022_Bennylin_14.jpg',
'maitreya.jpg':'https://upload.wikimedia.org/wikipedia/commons/e/e4/Maha_Vihara_Duta_Maitreya_Buddhist_Temple.jpg',
'paloh-naga.jpg':'https://thumb.viva.co.id/media/frontend/thumbs3/2021/06/11/60c2e5de1459f-sandiaga-uno-di-desa-wisata-denai-lama_1265_711.jpeg',
'bagan-percut.jpg':'https://cdn.placejoys.com/45959-oy-photo-1.jpg',
'lubuk-pakam.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/98/Welcome_gate_to_Lubuk_Pakam%2C_Deli_Serdang.jpg/960px-Welcome_gate_to_Lubuk_Pakam%2C_Deli_Serdang.jpg',
}
for name,url in items.items():
    req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
    data=urlopen(req,timeout=30).read()
    (base/name).write_bytes(data)
    print(name,len(data))
