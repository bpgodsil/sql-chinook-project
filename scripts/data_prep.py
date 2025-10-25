# data_prep.py
"""
Preprocessing script for Chinook music sales analysis.

This script:
1. Creates a clean `genre_music` view excluding non-music/TV genres.
2. Creates a `track_music` view filtered to valid genres.
3. Creates an `invoiceline_music` view filtered to valid tracks.

Usage:
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///path/to/chinook.db")
    import data_prep
    data_prep.prepare_music_views(engine)
"""

from sqlalchemy import text

# List of genres to exclude from analysis
NON_MUSIC_GENRES = ('TV Shows', 'Drama', 'Sci Fi & Fantasy', 'Comedy', 'Science Fiction')

def prepare_music_views(engine):
    """
    Drops and recreates the three filtered views:
      - genre_music
      - track_music
      - invoiceline_music
    """
    with engine.begin() as conn:
        # 1) genre_music
        conn.execute(text("DROP VIEW IF EXISTS genre_music;"))
        conn.execute(text(f"""
            CREATE VIEW genre_music AS
            SELECT GenreId, Name AS genre_name
            FROM genre
            WHERE Name NOT IN ('TV Shows', 'Drama', 'Sci Fi & Fantasy', 'Comedy', 'Science Fiction');
        """))

        # 2) track_music
        conn.execute(text("DROP VIEW IF EXISTS track_music;"))
        conn.execute(text("""
            CREATE VIEW track_music AS
            SELECT t.*
            FROM track AS t
            JOIN genre_music AS g ON g.GenreId = t.GenreId;
        """))

        # 3) invoiceline_music
        conn.execute(text("DROP VIEW IF EXISTS invoiceline_music;"))
        conn.execute(text("""
            CREATE VIEW invoiceline_music AS
            SELECT il.*
            FROM invoiceline AS il
            JOIN track_music AS t ON t.TrackId = il.TrackId;
        """))
