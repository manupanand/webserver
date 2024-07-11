#include <microhttpd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PORT 8888

static enum MHD_Result request_handler(void *cls, struct MHD_Connection *connection, 
                                       const char *url, const char *method, 
                                       const char *version, const char *upload_data, 
                                       size_t *upload_data_size, void **con_cls) {
    const char *response_text = "{\"message\": \"Hello, World!\"}";
    struct MHD_Response *response;
    enum MHD_Result ret;

    response = MHD_create_response_from_buffer(strlen(response_text), 
                                               (void *)response_text, 
                                               MHD_RESPMEM_PERSISTENT);
    MHD_add_response_header(response, "Content-Type", "application/json");
    ret = MHD_queue_response(connection, MHD_HTTP_OK, response);
    MHD_destroy_response(response);

    return ret;
}

int main() {
    struct MHD_Daemon *daemon;

    daemon = MHD_start_daemon(MHD_USE_INTERNAL_POLLING_THREAD, PORT, NULL, NULL, 
                              &request_handler, NULL, MHD_OPTION_END);
    if (NULL == daemon) {
        return 1;
    }

    printf("Server is running on port %d\n", PORT);
    getchar(); // Wait for user input to stop the server

    MHD_stop_daemon(daemon);
    return 0;
}