set(LIB_NAME wpAudio)

add_library(${LIB_NAME}
    STATIC
    SoundManager.cpp
)

target_link_libraries(${LIB_NAME}
PUBLIC
    wpUtils
PRIVATE
    wpFs
)
target_include_directories(${LIB_NAME} PUBLIC include PRIVATE include/Audio)
target_compile_options(${LIB_NAME} PRIVATE ${warn_opts})
set_property(TARGET ${LIB_NAME} PROPERTY POSITION_INDEPENDENT_CODE ON)
