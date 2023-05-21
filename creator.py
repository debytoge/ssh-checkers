import random


def generate_proxy_list(num_proxies):
    proxy_list = []
    for _ in range(num_proxies):
        ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        proxy = f"{ip}"
        proxy_list.append(proxy)
    return proxy_list


def save_proxies_to_file(proxy_list):
    with open('ips.txt', 'w') as proxy_file:
        for proxy in proxy_list:
            proxy_file.write(proxy + '\n')


def main():
    num_proxies = 100000  # Change this value to generate a different number of proxies
    proxies = generate_proxy_list(num_proxies)
    save_proxies_to_file(proxies)
    print('Generated proxies saved to ips.txt')


if __name__ == '__main__':
    main()
