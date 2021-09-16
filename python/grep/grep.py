def grep(pattern, flags, files):
    file_names = "-l" in flags
    line_numb = "-n" in flags
    lines = "-x" in flags
    case = "-i" in flags
    invert = "-v" in flags
    s_files = len(files) > 1

    memory = []

    for filename in files:
        with open(filename) as f:
            corr_lines = []

            for n, line in enumerate(f.readlines()):
                line = line.strip()
                if case:
                    pattrn = pattern.lower()
                    line_l = line.lower()
                else:
                    pattrn = pattern
                    line_l = line

                if (line_l == pattrn if lines else pattrn in line_l) ^ invert:
                    if line_numb:
                        line = str(n + 1) + ":" + line
                    if s_files:
                        line = filename + ":" + line

                    corr_lines.append(line + "\n")

            if file_names and corr_lines != []:
                memory.append(filename + "\n")
            else:
                memory.extend(corr_lines)

    return "".join(memory)
