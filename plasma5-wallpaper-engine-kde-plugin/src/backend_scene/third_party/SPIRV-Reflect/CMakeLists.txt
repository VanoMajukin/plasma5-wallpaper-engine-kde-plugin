project(spirv-reflect)

add_compile_definitions(SPIRV_REFLECT_ENABLE_ASSERTS=1)


add_library(${PROJECT_NAME} STATIC ${CMAKE_CURRENT_SOURCE_DIR}/spirv_reflect.h
                                     ${CMAKE_CURRENT_SOURCE_DIR}/spirv_reflect.c)

set_property(TARGET ${PROJECT_NAME} PROPERTY POSITION_INDEPENDENT_CODE ON)

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
