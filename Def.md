Statement := Assignment

Assignment := Variable "=" Expression

Expression := Primitive | Set | Operation | Variable

Primitive := "{}"

Operations := Union | Intersection | without | Equality

Union := Expression + Expression
Intersection := Expression i Expression
without := Expression / Expression
Equality := Expression == Expression