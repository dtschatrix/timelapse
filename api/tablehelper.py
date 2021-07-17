from sqlalchemy import engine
from sqlalchemy.sql.expression import insert
from . import tables
from .database import engine


def fill_up_base():
    #TODO add 8-10 cameras and rename prob
    stmt = (
        insert(tables.Cameras).
        values([{"camera_name": "camera1",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384304/ei/UFPwYLHXEJHxgAf0s69g/ip/109.86.185.70/id/73gIDMkV7_s.23/itag/95/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r2---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/T9/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/2/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgIQ-cuqsQbjZ_3bl42r-psG74f51k9iWcC0xRPDhz7xgCIQCKeyeufZvZAH7MjIMzDqvyFqCrdTpnl4-kgw4_EDFlfA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAK2Rn7811BaZBm01p3-qXttgxPtnIk-jE2DKjq1Yrlv2AiAbkhtm2X4I-ksLI3Y7KDsga0R1tRMTfejPwuHrXVKx_g%3D%3D/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera2",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384306/ei/UlPwYL36LOOKx_AP4p2DqAg/ip/109.86.185.70/id/Dsf2OfaqRL8.1/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r1---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/OZ/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/1/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRAIgFkcfnLL1HtJ3jWFtFX_0IgWZyFmWMNpcSlcjvtAOm70CIBKOsvpsBgYTd7WXdJfSswTTX_wea66xC3DMyURWJ1YZ/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRgIhAJ7RP3T3G0UMlBvkFWpqrvmxmrMORiQPMajlRytvtSSGAiEAmWzQjmDul4MZzsO0CpsfQASx36hknx4guA3tveFcV0s%3D/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera3",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384308/ei/VFPwYNMzhtuBB56GhdAK/ip/109.86.185.70/id/_BENPw-ZkRc.2/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r3---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/6I/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/3/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRAIgeSR3RaS-9Uzo_7i3QE1bGGIq5_frKBLnR-xzIJql8wYCICFpSdybaMYQdPo1YWNuwL0XSqi5L5m7BhIu7PgRDv-X/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRAIgWAOSkZhtrgWqar90C0WTVstHvOnQol4ROxiE4ARtBp8CIEXPMISgsYFsq86q9lRJ8qi72rLoQyaTXrjQzVBzJfuW/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera4",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384309/ei/VVPwYODyFZLVgAf_n7z4Cw/ip/109.86.185.70/id/5hHelJALhEo.4/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r4---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/e1/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/4/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIhANVHLRykOytD9kKy4_dwg6lEvc1TNc_-W1-kBhzkA-sWAiA6ZwcsQr83TyjT0YgKg9H2kuPwG_x1C31izm5WOB3HjQ%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRgIhAJucLgj37Ftpns7swb0y1IGdheoLDpTaiSOmUi01dooiAiEA0h4bCT8vGF8vmF8k6d8czPTK1rqT5NLWQ0Wyd-sfV5g%3D/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera5",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384310/ei/VlPwYNinMoShx_APiPKO6Ag/ip/109.86.185.70/id/4qyZLflp-sI.3/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r4---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/OR/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/4/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgEmm8nEU978LSwoJIGBmy9WF4b7QYkejCBRBSEAhHp4ECIQCvJe_3foRIniiJCLvEwb3prTkPK0yCsqx6yVh8amKD1g%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIgdEGUm8MPl62GeLidtAJFXvb1XxczUpxYxy5_1dvklRMCIQCDFZXIANEJ6czHwscv72R-TWlGZIMZisik7RrRyjrydQ%3D%3D/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera6",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384312/ei/WFPwYLvIC8bE7gOXkb2ADg/ip/109.86.185.70/id/OcrV35VFsok.3/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r3---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/H9/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/3/pcm2cms/yes/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIhALVcmfz8f6zPLj-IhiQ2nqFLUxC3FCTsO2Czh1cQPqU9AiA3JEKki3NybEQ0PLPEgo71QPnz8BGoOtx0y1QKAu6eVQ%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pcm2cms,pl/lsig/AG3C_xAwRAIgFGf-9gjn8hh5jBr2i9wfy_m5IUGgwy9zEh1lnRiGMjwCICd9mP4kbAesLCbM9edPZCB0OUL14Lq0uR6MfjkXRN_1/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera7",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384318/ei/XVPwYMG7PNjh-gbjrrKgAQ/ip/109.86.185.70/id/oSoR2qsv7es.5/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r3---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/w0/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/3/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRgIhAJvNoZhpzvxRGnnR4f9GF5vvm2jkN3g0ikMN4EdGgAiAAiEAgQCbd2fcrjhDuzgRO0_AGveD03CCtSOZUawSCbTNQmg%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAM9n3BqJOEy4QsLI9jEeXUDFcflsEToknKuGUvTisBFlAiBl5TdnzfQyn6WviJxnJQb5llZh1Y9voC07PRc5qYUh3w%3D%3D/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera8",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384319/ei/X1PwYP_mItSzgAeq2ZKoBQ/ip/109.86.185.70/id/fYoP5VLgetY.1/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r4---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/C0/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/4/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIhAI7NtbqeQh_tEPZrykUTtMSaD4JpzV2p8FPOFqn1SnOGAiB4DCCm1Zx38Q-RiFPMef32Rob-Ls-uYmhNbR8YmI8W4w%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRAIgeYAEz-XSPZ9US52tH9Oq8n7PUKKQjXMBsOSMHXubmSMCIHOmpuerCkMiWVIjtWKWbenwcvaxhWAJZtHtzK2l1DAz/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera9",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384321/ei/YVPwYPetEJaE-gaCuLmIBA/ip/109.86.185.70/id/PWKjaA-wNho.2/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r3---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/jA/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/3/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIhAMujZGeV1u5mmN5F_qzHZ4rm2CWmxn3m4kPgZGYUs6UaAiA8BYrpwBGLwcNS4JN2Y9FmtjzUGl_DykSJrweDoymR9A%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRAIgJc5J1_JSsvnQmAxTTKdNS7WBWNKrhcZBkJ5WaonzjTsCIEK2QwywwKfyV4iW_VZGQGrayGacqHf_QpLRuvSj1NAd/playlist/index.m3u8",
                 "is_active": True},
                {"camera_name": "camera10",
                 "stream_url": "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1626384327/ei/Z1PwYMiDBMbrgAe0zK_YDA/ip/109.86.185.70/id/xWAaC3MuaZQ.3/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/hls_chunk_host/r1---sn-ugpva5o-ig3s.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/12400/mh/YI/mm/44/mn/sn-ugpva5o-ig3s/ms/lva/mv/m/mvi/1/pl/24/dover/11/keepalive/yes/fexp/24001373,24007246/mt/1626361012/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRgIhAIi3NV5ntWnv3algW9t2JyZ8xLjm4n1SGLlVpQdx3g0FAiEA_bpnBt7QNXVX1orJNBMI2fBNhxTktXy2_bTMv7lvL5c%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRAIgX7XrBA6j6xRw5Gg5sGU258q79-dZnMwZ-K6NQkSoTAQCIBGUmHSpA36bGfSyCwhQBLgfGv5JZRTHpQSqbKAQ2pSA/playlist/index.m3u8",
                 "is_active": True}])
    )

    conn = engine.connect()
    conn.execute(stmt)
    conn.close()
