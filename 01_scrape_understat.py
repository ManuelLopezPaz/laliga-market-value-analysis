import time
import requests
import json
import pandas as pd

url_api    = "https://understat.com/main/getPlayersStats/"
liga       = "La liga"
temporadas = list(range(2014, 2025))
espera     = 2  # espero un poco para no saturar el servidor

# no estoy seguro si siempre están todas
columnas = [
    "id", "player_name", "games", "time", "goals", "xG",
    "assists", "xA", "shots", "key_passes",
    "position", "team_title", "npg", "npxG",
]

headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest",
}


def obtener_temporada(season):
    params = {"league": liga, "season": str(season)}

    # a veces falla, por eso el try
    try:
        resp = requests.post(url_api, data=params, headers=headers, timeout=20)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"error en la temporada {season}: {e}")
        return None

    if not data.get("success") or "players" not in data:
        print(f"algo salió mal en temporada {season}: {list(data.keys())}")
        return None

    players = data["players"]
    print(f"  jugadores encontrados: {len(players)}")

    df = pd.DataFrame(players)

    columnas_presentes = [c for c in columnas if c in df.columns]
    columnas_faltantes = [c for c in columnas if c not in df.columns]
    if columnas_faltantes:
        print(f"  aviso: no encontré estas columnas: {columnas_faltantes}")

    df = df[columnas_presentes].copy()
    df.rename(columns={"id": "player_id"}, inplace=True)
    df["season"] = f"{season}/{str(season + 1)[-2:]}"

    return df


def main():
    todos_los_datos = []

    for season in temporadas:
        etiqueta = f"{season}/{str(season + 1)[-2:]}"
        print(f"\ntemporada {etiqueta}")

        df_temporada = obtener_temporada(season)

        if df_temporada is not None:
            todos_los_datos.append(df_temporada)
            print(f"  añadido: {df_temporada.shape}")

        if season < temporadas[-1]:
            time.sleep(espera)

    if not todos_los_datos:
        print("no se obtuvo nada, algo falló")
        return

    df_total = pd.concat(todos_los_datos, ignore_index=True)

    output_file = "understat_laliga_2014_2024.csv"
    df_total.to_csv(output_file, index=False, encoding="utf-8")

    print(f"listo. {df_total.shape[0]} filas en total")
    print(f"temporadas: {sorted(df_total['season'].unique())}")
    print(f"guardado en {output_file}")


if __name__ == "__main__":
    main()
