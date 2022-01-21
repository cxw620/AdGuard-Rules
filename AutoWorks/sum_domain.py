import re

def sum_domain(__file_path__, __file_name__):
    domain_dist = {}
    with open(__file_path__ + __file_name__, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line:
                # 首先判断是不是注释
                anno = re.search(r"^\s{0,}#.*|^\s{0,}!.*", line)
                if anno:
                    continue
                line_list = list(line)
                line_list_reversed = list(reversed(list(line_list)))
                count = 0
                first_stop = False
                domain = ""
                for character in line_list_reversed:
                    if character == "^":
                        split_loc_end = count + 1
                        continue
                    if character == "." and first_stop:
                        split_loc_start = count + 1
                        for i in range(split_loc_end, split_loc_start, 1):
                            domain = str(line_list_reversed[i]) + domain
                        break
                    elif character == ".":
                        first_stop = True
                    count += 1
                if domain:
                    try:
                        domain_dist[domain] += 1
                    except:
                        domain_dist[domain] = 1
        else:
            domain_list = list(domain_dist.items())
            with open(__file_path__ + "domain_list.txt", "w+") as rt:
                for domain_info in domain_list:
                    rt.write(domain_info + "\n")
