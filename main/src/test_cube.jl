cfunc = (x,y,z)->ccall((:cube,"./so/libcube.so"),Float64,(Float64,Float64,Float64),x,y,z)
println(cfunc(3.0,4.0,5.0))
