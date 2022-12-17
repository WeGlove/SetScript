## Statements
- Statement := ((Assignment | While | Function | Return | Expression | Import | If | Namespace) ";") | EmptyStatement
- Assignment := Variable "=" Expression
- While := "while" "(" Expression ")" "{" [Statement]*"}"
- For := "for" "(" statement ";" statement ";" statement ")" "{" [statement]*"}"
- Function := "def" Identifier "(" [Expression \[, Expression\]\*] ")" "{" Statement* "}"
- Return := "return" Expression
- Import := "import" Path
- If := "if" "(" Expression ")" "then" "{" [Statement]* "}" "else" "{" [Statement]* "}"
- Namespace := "namespace" "(" Identifier "")" "{" [Statement]* "}"
- EmptyStatement := ";"

## Expressions
- Expression := Set | Operation | Variable | Parentheses | Tuple | FunctionCall | Power | Number
- Set := "{"[Expression \[, Expression\]\*]*"}"
- Function_Call := Identifier([Expression \[, Expression\]\*])
- Power := "P" "(" Expression ")"
- Tuple := "<"[Expression \[, Expression\]\*]*">"
- Parenthesis := "(" Expression ")"
- Number := (0|1|2|3|4|5|6|7|8|9)+

### Operations
- Operations := Binary_Operations | Unariy Operations
- Binary_Operations := Union | Intersection | Difference | In | Equality | Inequality
- Unariy_Operations := BigUnion | BigIntersection

#### Binary Operations

- Union := Expression | Expression
- Intersection := Expression & Expression
- Difference := Expression - Expression
- In := Expression "in" Expression
- Equality := Expression "==" Expression
- Inequality := Expression "!=" Expression

#### Unariy Operations
- BigUnion := "||" Expression
- BigIntersection := "&&" Expression

## Misc
- Identifier := ([A..Z|a..z])*
- Qualified_Identifier := Identifier ["." Identifier]*
- Path := A file path
