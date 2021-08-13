import sqlalchemy as sa
from sqlalchemy import engine
from sqlalchemy.sql.expression import insert
import tables as tables
from database import engine


def fill_up_base():
    stmt = (
        insert(tables.Cameras).
        values([{"camera_name": "camera1",
                 "stream_url": "https://www.youtube.com/watch?v=mTohI_JwYxE",
                 "is_active": True},
                {"camera_name": "camera2",
                 "stream_url": "https://www.youtube.com/watch?v=HpZAez2oYsA",
                 "is_active": True},
                {"camera_name": "camera3",
                 "stream_url": "https://www.youtube.com/watch?v=nprdq03e8yI",
                 "is_active": True},
                {"camera_name": "camera4",
                 "stream_url": "https://www.youtube.com/embed/5hHelJALhEo?autoplay=1&controls=1&rel=0&showinfo=0&iv_load_policy=3&cc_load_policy=0&cc_lang_pref=en&wmode=transparent&modestbranding=1&disablekb=1&origin=http%3A%2F%2Fwebcam.scs.com.ua&enablejsapi=1&widgetid=4",
                 "is_active": True},
                {"camera_name": "camera5",
                 "stream_url": "https://www.youtube.com/watch?v=mNECPewguNU",
                 "is_active": True},
                {"camera_name": "camera6",
                 "stream_url": "https://www.youtube.com/embed/4qyZLflp-sI?autoplay=1&controls=1&rel=0&showinfo=0&iv_load_policy=3&cc_load_policy=0&cc_lang_pref=en&wmode=transparent&modestbranding=1&disablekb=1&origin=http%3A%2F%2Fwebcam.scs.com.ua&enablejsapi=1&widgetid=4",
                 "is_active": True},
                {"camera_name": "camera7",
                 "stream_url": "https://www.youtube.com/embed/OcrV35VFsok?autoplay=1&controls=1&rel=0&showinfo=0&iv_load_policy=3&cc_load_policy=0&cc_lang_pref=en&wmode=transparent&modestbranding=1&disablekb=1&origin=http%3A%2F%2Fwebcam.scs.com.ua&enablejsapi=1&widgetid=4",
                 "is_active": True},
                {"camera_name": "camera8",
                 "stream_url": "https://www.youtube.com/embed/oSoR2qsv7es?autoplay=1&controls=1&rel=0&showinfo=0&iv_load_policy=3&cc_load_policy=0&cc_lang_pref=en&wmode=transparent&modestbranding=1&disablekb=1&origin=http%3A%2F%2Fwebcam.scs.com.ua&enablejsapi=1&widgetid=4",
                 "is_active": True},
                {"camera_name": "camera9",
                 "stream_url": "https://www.youtube.com/embed/fYoP5VLgetY?autoplay=1&controls=1&rel=0&showinfo=0&iv_load_policy=3&cc_load_policy=0&cc_lang_pref=en&wmode=transparent&modestbranding=1&disablekb=1&origin=http%3A%2F%2Fwebcam.scs.com.ua&enablejsapi=1&widgetid=4",
                 "is_active": True},
                {"camera_name": "camera10",
                 "stream_url": "https://www.youtube.com/embed/PWKjaA-wNho?autoplay=1&controls=1&rel=0&showinfo=0&iv_load_policy=3&cc_load_policy=0&cc_lang_pref=en&wmode=transparent&modestbranding=1&disablekb=1&origin=http%3A%2F%2Fwebcam.scs.com.ua&enablejsapi=1&widgetid=4",
                 "is_active": True}])
    )

    conn = engine.connect()
    conn.execute(stmt)
    conn.close()


def tables_exist() -> bool:
    inspect = sa.inspect(engine)
    if len(inspect.get_table_names()) > 0:
        return True
    return False
