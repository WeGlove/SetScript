## Statements
- Statement := (Assignment | While | Function | Return | Expression | Import | If) ";"
- Assignment := Variable "=" Expression
- While := "while" "(" Expression ")" "{" [Statement]*"}"
- For := "for" "(" statement ";" statement ";" statement ")" "{" [statement]*"}"
- Function := "def" Identifier "(" [Expression \[, Expression\]\*] ")" "{" Statement* "}"
- Return := "return" Expression
- Import := "import" Path
- If := "if" "(" Expression ")" "then" "{" [Statement]* "}" "else" "{" [Statement]* "}"

## Expressions
- Expression := Set | Operation | Variable | Parentheses
- Set := "{"[Expression \[, Expression\]\*]*"}"
- Function_Call := Identifier
- Tuple := "<"[Expression \[, Expression\]\*]*">"
- Parenthesis := "(" Expression ")"

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
- Path := A file path
