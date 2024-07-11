static int request_handler(void *cls, struct MHD_Connection *connection, 
                           const char *url, const char *method, 
                           const char *version, const char *upload_data, 
                           size_t *upload_data_size, void **con_cls) {
    const char *response_text;
    struct MHD_Response *response;
    int ret;

    if (strcmp(url, "/api/v1/resource") == 0 && strcmp(method, "GET") == 0) {
        response_text = "{\"message\": \"Resource data\"}";
    } else if (strcmp(url, "/api/v1/resource") == 0 && strcmp(method, "POST") == 0) {
        // Handle POST request
        response_text = "{\"message\": \"Resource created\"}";
    } else {
        response_text = "{\"error\": \"Not found\"}";
        response = MHD_create_response_from_buffer(strlen(response_text), 
                                                   (void *)response_text, 
                                                   MHD_RESPMEM_PERSISTENT);
        MHD_add_response_header(response, "Content-Type", "application/json");
        ret = MHD_queue_response(connection, MHD_HTTP_NOT_FOUND, response);
        MHD_destroy_response(response);
        return ret;
    }

    response = MHD_create_response_from_buffer(strlen(response_text), 
                                               (void *)response_text, 
                                               MHD_RESPMEM_PERSISTENT);
    MHD_add_response_header(response, "Content-Type", "application/json");
    ret = MHD_queue_response(connection, MHD_HTTP_OK, response);
    MHD_destroy_response(response);

    return ret;
}
