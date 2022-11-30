## Statements
Statement := (Assignment | While) ";"
Assignment := Variable "=" Expression
While := "while" "(" Expression ")" "{" [Statement]*"}"

## Expressions
Expression := Set | Operation | Variable
Set := "{"[Expression \[, Expression\]\*]*"}"

### Operations
Operations := Union | Intersection | Difference | In | Equality
Union := Expression | Expression
Intersection := Expression & Expression
Difference := Expression - Expression
In := Expression "in" Expression
Equality := Expression "==" Expression
