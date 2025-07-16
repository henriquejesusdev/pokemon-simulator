import asyncio
import random
import time

# Listas de Pokémons por região
KANTO_POKEMONS = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Eevee"]
JOHTO_POKEMONS = ["Chikorita", "Cyndaquil", "Totodile", "Togepi", "Mareep"]
HOENN_POKEMONS = ["Treecko", "Torchic", "Mudkip", "Ralts", "Bagon"]

async def busca_pokemon_kanto():
    """Simula a busca de um Pokémon na região de Kanto."""
    tempo_busca = random.uniform(1, 5)
    await asyncio.sleep(tempo_busca)
    pokemon = random.choice(KANTO_POKEMONS)
    print(f"Pokémon encontrado em Kanto: {pokemon} (tempo: {tempo_busca:.2f} segundos)")
    return pokemon

async def busca_pokemon_johto():
    """Simula a busca de um Pokémon na região de Johto."""
    tempo_busca = random.uniform(1, 5)
    await asyncio.sleep(tempo_busca)
    pokemon = random.choice(JOHTO_POKEMONS)
    print(f"Pokémon encontrado em Johto: {pokemon} (tempo: {tempo_busca:.2f} segundos)")
    return pokemon

async def busca_pokemon_hoenn():
    """Simula a busca de um Pokémon na região de Hoenn."""
    tempo_busca = random.uniform(1, 5)
    await asyncio.sleep(tempo_busca)
    pokemon = random.choice(HOENN_POKEMONS)
    print(f"Pokémon encontrado em Hoenn: {pokemon} (tempo: {tempo_busca:.2f} segundos)")
    return pokemon

async def main():
    """Função principal que coordena a busca simultânea de Pokémons."""
    print("Iniciando a busca de Pokémons em Kanto, Johto e Hoenn...")
    start_time = time.perf_counter()
    
    resultados = await asyncio.gather(
        busca_pokemon_kanto(),
        busca_pokemon_johto(),
        busca_pokemon_hoenn()
    )
    
    end_time = time.perf_counter()
    tempo_total = end_time - start_time
    
    print("\nResultados da busca:")
    print(f" - Kanto: {resultados[0]}")
    print(f" - Johto: {resultados[1]}")
    print(f" - Hoenn: {resultados[2]}")
    print(f"Tempo total de busca: {tempo_total:.2f} segundos")

def run():
    """Função síncrona para executar a função assíncrona main."""
    asyncio.run(main())

if __name__ == "__main__":
    run()