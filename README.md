# myownlang

Python製の自作インタプリタ言語。文はALGOL風だが、式はLISP風。何も勉強せずに作ったのでとても非効率。ASTを使っておらず再帰が変でバグがあるかも。関数が実装できなさそうな事に気づいたので（ほぼ）開発終了。

演算子など: 
`END`,`PRINT`,`DEFVAR`,`ASSIGN`,`(`,`)`,`+`,`-`,`*`,`/`,`>`,`<`,`>=`,`<=`,`==`,`!=`,`&`,`|`,`IF`,`WHILE`,`{`,`}`,`INPUT`,`EVAL`

Python上でHello world:
```
from myownlang import *

src = """
PRINT 42
END
"""

main(src, debug_mode=0)
```

ターミナル上でHello world:
```
python myownlang.py "
PRINT 42
END
"
```

FizzBuzz: 
```
DEFVAR x
ASSIGN x 1
DEFVAR xmax
INPUT xmax
WHILE (<= x xmax) {
    IF (== 0 (% x 3)) {
        IF (== 0 (% x 5)) {
            PRINT 333555
        }
        IF (!= 0 (% x 5)) {
            PRINT 333
        }
    }
    IF (!= 0 (% x 3)) {
        IF (== 0 (% x 5)) {
            PRINT 555
        }
        IF (!= 0 (% x 5)) {
            PRINT x
        }
    }
    ASSIGN x (+ x 1)
}
END
```
