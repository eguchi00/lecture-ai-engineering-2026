# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：講座固有の質問に対して用語集を検索し正しい答えを回答した
- `--trace` で見えたツール呼び出し（ツール名と引数）：
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[usage] RunUsage(cost=Decimal('0.0008794'), details={'text_prompt_tokens': 1148}, input_text_tokens=1148, input_tokens=1148, output_tokens=214, requests=2, tool_calls=2)
- 1つの質問での LLM 呼び出し回数（`requests`）：2回
- 追加したツールと、docstring に書いた説明：Copilotを使って、tools.pyに確認問題を出すmake_quiz(lecture)を追加するととに、agent.pyに登録し確認問題時に利用する指示を追加した。make_quiz(lecture)の内容は以下の通り。
〇指定回の用語をランダムに選択
〇問題と定義を JSON で返却
〇用語がない回は明示的なメッセージを返却
docstringに書いた説明は以下の通り
def make_quiz(lecture: int) -> str:
    """指定した回の用語集から、学習用の確認問題を1問作って返す。

    「第N回の確認問題を出して」と頼まれたときに使う。返り値は問題文と
    用語の定義を含む JSON 文字列で、エージェントが問題を出題するときに利用する。
    """


## 宿題

- 取り組んだレベル：基礎
- やったこと：INSTRUCTIONS から「必ず search_glossary で用語集を確認する」の行を消して回答がどのように変わるか比較
make_quizのdocstring の「用語を1つ」を「まとめて」に変えて、検索の回数がどう変わるか
- 結果：回答結果や検索の回数は変わらなかった
- 気づき・疑問：make_quizのdocstringを変えても検索回数が変わらなかったのはやり方が間違っているのか、それで正しいのか分からなかったので、次回の講義で宿題の解説をしてもらえると幸いです。
