def main(args):
	settings = { "wait": 0.1 }
	def set_wait(arg_str):
		settings["wait"] = float(arg_str)

	arg_reader = {
		#argument key: (read, do-function)
		"--wait":    (1, set_wait),
		"--no-wait": (0, lambda: set_wait(0)),
	}
	# read, do = arg_reader["--wait"]

	a = 0
	while a < len(args):
		arg = args[a]
		try:
			read, do = arg_reader[arg]
			next_a = a + 1 + read
			more_args = args[a + 1 : next_a]
			do(*more_args)
			a = next_a
		except:
			print(f"argument {arg} not understood!")
			a += 1
