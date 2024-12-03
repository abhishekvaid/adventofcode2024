import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day2Part2 {

    private static boolean isSafe2(ArrayList<Integer> lst) {
        if (isSafe(lst)) {
            return true;
        }
        for (int i = 0 ; i < lst.size() ; i++) {
            var newList = new ArrayList<>(lst);
            newList.remove(i);
            if (isSafe(newList)) {
                return true;
            }
        }
        return false;
    }

    private static boolean isSafe(ArrayList<Integer> lst) {
        if (lst.get(1) - lst.get(0) == 0)
            return false;
        boolean isPositive = lst.get(1) - lst.get(0) > 0;
        return IntStream
                .range(0, lst.size() - 1)
                .map(i -> lst.get(i + 1) - lst.get(i))
                .allMatch(
                        diff ->
                                diff != 0
                                && Math.abs(diff) >= 1
                                && Math.abs(diff) <= 3
                                && diff > 0 == isPositive
                );
    }

    public static void main(String[] args) throws IOException {
        var res = Files.lines(Path.of("input.txt"))
                .map(
                        line -> Arrays.stream(line.split("\\s+"))
                                .map(Integer::parseInt)
                                .collect(Collectors
                                        .toCollection(ArrayList<Integer>::new)))
                .map(Day2Part2::isSafe2)
                .filter( safe -> safe)
                .count()
        ;
        System.out.println(res);
    }
}
