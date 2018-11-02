cfunc = (x,y)->ccall((:mean,"libmean.so"),Float64,(Float64,Float64),x,y)
println(cfunc(3.0,4.0))
