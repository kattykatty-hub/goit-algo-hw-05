import timeit

from algorithms import rabin_karp_search, boyer_moore_search, knut_morris_pratt_search

if __name__ == '__main__':
    for text_path in ["стаття 1.txt", "стаття 2.txt"]:
        print(f"Тест проведений на статті {text_path}:")
        with open(text_path, encoding='utf-8') as f:
            text = f.read()
        for pattern, pattern_name in zip(
                ["що",            "розроб",           "@$"                     , "@.$0?!"],
                ["коротке слово", "чуть довше слово", "коротке випадкове слово", "чуть довше випадкове слово"]
        ):
            print(f"\t{pattern_name=}")
            for search_alg, search_alg_name in zip(
                    [rabin_karp_search, boyer_moore_search, knut_morris_pratt_search],
                    ["\"Rabin Karp Search\"       ", "\"Boyer Moore Search\"      ", "\"Knut Morris Pratt Search\""]
            ):
                time_taken = timeit.timeit(lambda: search_alg(text, pattern), number=5)
                print(f"\t\tTime taken to search substring {repr(pattern)} with {search_alg_name} in seconds: {time_taken:.5f}")
        print("-----------------------------------------------------------------")
