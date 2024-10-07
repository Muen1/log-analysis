def read_log_file(log_file_path):
    ip_counts = {}  # Dictionary to store IP addresses and their request counts
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            ip, count = line.strip().split(',')
            ip_counts[ip] = int(count)
    return ip_counts

def get_top_n_ips(ip_counts, n):
    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_ips[:n]

def write_output_file(output_file_path, top_ips):
    with open(output_file_path, 'w') as output_file:
        for importance, (ip, count) in enumerate(top_ips, start=1):
            output_file.write(f"{importance},{ip},{count}\n")

if __name__ == "__main__":
    log_file_path = "logs/sample_01_easy.log"
    n = 3  # You can adjust this value as needed
    ip_counts = read_log_file(log_file_path)
    top_ips = get_top_n_ips(ip_counts, n)
    output_file_path = f"logs/sample_01_easy_result_n{n}.txt"
    write_output_file(output_file_path, top_ips)
    print(f"Top {n} IP addresses written to {output_file_path}")

