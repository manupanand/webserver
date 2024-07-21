#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define DNS_PORT 53
#define DNS_SERVER "8.8.8.8" // Google's Public DNS Server

#pragma pack(push, 1)
// DNS header structure
struct dns_header {
    unsigned short id; // identification number
    unsigned char rd :1; // recursion desired
    unsigned char tc :1; // truncated message
    unsigned char aa :1; // authoritive answer
    unsigned char opcode :4; // purpose of message
    unsigned char qr :1; // query/response flag

    unsigned char rcode :4; // response code
    unsigned char cd :1; // checking disabled
    unsigned char ad :1; // authenticated data
    unsigned char z :1; // its z! reserved
    unsigned char ra :1; // recursion available

    unsigned short q_count; // number of question entries
    unsigned short ans_count; // number of answer entries
    unsigned short auth_count; // number of authority entries
    unsigned short add_count; // number of resource entries
};

// Question structure
struct question {
    unsigned short qtype;
    unsigned short qclass;
};

// Resource record structure
struct r_data {
    unsigned short type;
    unsigned short _class;
    unsigned int ttl;
    unsigned short data_len;
};
#pragma pack(pop)

// Function to change a hostname to DNS format
void ChangetoDnsNameFormat(unsigned char* dns, unsigned char* host) {
    int lock = 0, i;
    strcat((char*)host, ".");
    for(i = 0; i < strlen((char*)host); i++) {
        if(host[i] == '.') {
            *dns++ = i - lock;
            for(; lock < i; lock++) {
                *dns++ = host[lock];
            }
            lock++;
        }
    }
    *dns++ = '\0';
}

int main(int argc, char *argv[]) {
    unsigned char buf[65536], *qname;
    struct dns_header *dns = NULL;
    struct sockaddr_in dest;

    // Check for proper input
    if(argc < 2) {
        printf("Usage: %s <hostname>\n", argv[0]);
        return 1;
    }

    // Create a socket
    int s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if(s < 0) {
        perror("socket failed");
        return 1;
    }

    // Configure the destination server
    dest.sin_family = AF_INET;
    dest.sin_port = htons(DNS_PORT);
    dest.sin_addr.s_addr = inet_addr(DNS_SERVER);

    // DNS header
    dns = (struct dns_header*)&buf;
    dns->id = (unsigned short) htons(getpid());
    dns->qr = 0; // This is a query
    dns->opcode = 0; // Standard query
    dns->aa = 0; // Not Authoritative
    dns->tc = 0; // Not Truncated
    dns->rd = 1; // Recursion Desired
    dns->ra = 0; // Recursion not available
    dns->z = 0;
    dns->ad = 0;
    dns->cd = 0;
    dns->rcode = 0;
    dns->q_count = htons(1); // We have only one question

    // Point to the query portion
    qname = (unsigned char*)&buf[sizeof(struct dns_header)];
    ChangetoDnsNameFormat(qname, (unsigned char*)argv[1]);

    // Set the question
    struct question *qinfo = (struct question*)&buf[sizeof(struct dns_header) + (strlen((const char*)qname) + 1)];
    qinfo->qtype = htons(1); // Type A
    qinfo->qclass = htons(1); // Class IN

    // Send the DNS query
    if(sendto(s, (char*)buf, sizeof(struct dns_header) + (strlen((const char*)qname) + 1) + sizeof(struct question), 0, (struct sockaddr*)&dest, sizeof(dest)) < 0) {
        perror("sendto failed");
    }

    // Receive the DNS response
    int i = sizeof(dest);
    if(recvfrom(s, (char*)buf, 65536, 0, (struct sockaddr*)&dest, (socklen_t*)&i) < 0) {
        perror("recvfrom failed");
    }

    // Print the response
    dns = (struct dns_header*)buf;
    printf("The response contains : ");
    printf("\n %d Questions.", ntohs(dns->q_count));
    printf("\n %d Answers.", ntohs(dns->ans_count));
    printf("\n %d Authoritative Servers.", ntohs(dns->auth_count));
    printf("\n %d Additional records.\n\n", ntohs(dns->add_count));

    // Close the socket
    close(s);
    return 0;
}