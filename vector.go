package main

import (
	"math"
)

type Vector struct {
	x, y, z float64
}

func Add(u, v Vector) Vector {
	return Vector{
		v.x + u.x,
		v.y + u.y,
		v.z + u.z,
	}
}

func Subtract(u, v Vector) Vector {
	return Vector{
		v.x - u.x,
		v.y - u.y,
		v.z - u.z,
	}
}

func Multiply(u, v Vector) Vector {
	return Vector{
		v.x * u.x,
		v.y * u.y,
		v.z * u.z,
	}
}

func Sum(v Vector) float64 {
	return v.x + v.y + v.z
}

func Dot(u, v Vector) float64 {
	return v.x*u.x + v.y*u.y + v.z*u.z
}

func Norm(v Vector) Vector {
	m := Magnitude(v)
	return Vector{
		v.x / m,
		v.y / m,
		v.z / m,
	}
}

func Magnitude(v Vector) float64 {
	return math.Pow( Sum(Multiply(v, v)), 0.5 )
}
