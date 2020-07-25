function diamond(n)
{
	if (n < 0 || n % 2 == 0) return null
    const midpoint = (n - 1) / 2
    const spaces = x => Math.abs(x - midpoint)
    const filled = x => n - 2 * Math.abs(x-midpoint)
    const layer = l => " ".repeat(spaces(l)) + "*".repeat(filled(l)) + "\n"
	return [ ...Array(n).keys()].reduce((d, l) => d + layer(l), "")
}

//diamond(1)
//diamond(3)
//diamond(5)