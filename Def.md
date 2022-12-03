## Statements
- Statement := (Assignment | While | Function | Return | Expression) ";"
- Assignment := Variable "=" Expression
- While := "while" "(" Expression ")" "{" [Statement]*"}"
- For := "for" "(" statement ";" statement ";" statement ")" "{" [statement]*"}"
- Function := "def" Identifier "(" [Expression \[, Expression\]\*] ")" "{" Statement* "}"
- Return := "return" Expression

## Expressions
- Expression := Set | Operation | Variable | Parentheses
- Set := "{"[Expression \[, Expression\]\*]*"}"
- Function_Call := Identifier
- Tuple := "<"[Expression \[, Expression\]\*]*">"
- Parenthesis := "(" Expression ")"

### Operations
- Operations := Union | Intersection | Difference | In | Equality | Inequality
- Union := Expression | Expression
- Intersection := Expression & Expression
- Difference := Expression - Expression
- In := Expression "in" Expression
- Equality := Expression "==" Expression
- Inequality := Expression "!=" Expression

## Misc
- Identifier := ([A..Z|a..z])*
